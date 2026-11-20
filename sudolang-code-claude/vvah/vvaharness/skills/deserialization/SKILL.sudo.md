# vvaharness/skills/deserialization/SKILL.md

A lens for unsafe deserialization of attacker-influenced bytes, chiefly on the JVM.

Source: `vvaharness/skills/deserialization/SKILL.md` (lines 1-51)
Executor: model (instructions only; no code checks any rule in this file)
Called from: copied into `.vvaharness/skills/deserialization/` of the scanned repository by `vvaharness/skills/__init__.py` inject_skills; reachable from Stage 2 and Stage 4 model sessions through `skill_root`

// external: the frontmatter `description` is what the agent backend shows the model when it decides whether to load this skill; that selection happens in the backend (`vvaharness/backends/`), outside this batch.
// abstracted: lines 6-20 are the Apache 2.0 license comment; no instruction.

// prompt-src: vvaharness/skills/deserialization/SKILL.md:1-51
DeserializationLens {
  name: "deserialization"
  description: "Find unsafe deserialization of untrusted data: pickle, yaml.load, native object streams, and type-confusable decoders that instantiate attacker-chosen classes."
  role: "You are an Unsafe-deserialization expert."   // prompt-src: vvaharness/skills/deserialization/SKILL.md:24-24
  Constraints {
    // prompt-src: vvaharness/skills/deserialization/SKILL.md:24-26
    Hunt for deserialization of attacker-influenced bytes through libraries that invoke code during object reconstruction — "the dominant remote-code-execution vector on the JVM."

    // prompt-src: vvaharness/skills/deserialization/SKILL.md:28-34
    constraint HardGate {
      "HARD GATE — a finding requires BOTH:
        (a) a deserializer call site, AND
        (b) a path from untrusted input (HTTP body/header/param, message queue, file upload, cache, DB blob written by another tenant) to that call."
      "Deserializing your own freshly-serialized data, or data signed/HMAC'd before serialize and verified before deserialize, is NOT a finding."
      "Cite both file:line points or drop it."
    }

    // prompt-src: vvaharness/skills/deserialization/SKILL.md:36-51 — "Where to look first (non-exhaustive — reason beyond this list)"
    Java native: ObjectInputStream.readObject / readUnshared, readObject / readResolve overrides, RMI / JMX / JNDI endpoints, Apache Commons SerializationUtils.
    Jackson: enableDefaultTyping / activateDefaultTyping, @JsonTypeInfo(use = Id.CLASS or Id.MINIMAL_CLASS), a LaissezFaire PolymorphicTypeValidator, polymorphic fields typed Object or Serializable.
    XML: XMLDecoder, XStream without a hardened allow-list, JAXB XmlAdapter instantiating by class name.
    YAML: SnakeYAML new Yaml() / Yaml(new Constructor()) on untrusted input; "only SafeConstructor is safe."
    Others: Kryo, Hessian / Burlap, FST, Spring DefaultDeserializer, RedisTemplate with JdkSerializationRedisSerializer on a shared Redis.
    Mitigation check: is an ObjectInputFilter / serialFilter / class allow-list applied BEFORE readObject; if so, judge whether the allow-list itself admits a known gadget (for example java.util.*, org.apache.commons.*).
  }
}
