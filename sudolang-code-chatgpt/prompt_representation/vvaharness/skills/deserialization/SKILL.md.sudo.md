# vvaharness/skills/deserialization/SKILL.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Untrusted reconstruction gate

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/skills/deserialization/SKILL.md:24-51
Constraints {
  Requested evidence includes both a deserializer call and an untrusted HTTP/message/upload/cache/cross-tenant-DB flow to it, with both file:line references.
  if (the bytes are freshly self-serialized, or serialization is signed/HMACed and verified before reconstruction) { The requested disposition is no finding. }
  if (both source and call evidence cannot be cited) { The model is asked to drop the candidate. }
  The non-exhaustive search covers native JVM reconstruction/RMI/JMX/JNDI, permissive Jackson typing, XMLDecoder/XStream/JAXB class loading, unsafe SnakeYAML constructors, Kryo/Hessian/Burlap/FST/Spring/Redis serializers.
  if (an ObjectInputFilter, serialFilter or class allow-list precedes reconstruction) {
    The model is asked to judge whether its admitted classes still contain gadgets, including broad java.util.* or org.apache.commons.*.
  }
}
```

Supply relationship: skills/__init__.py discovers SKILL.md packages and injects temporary copies; S4/S6 route options decide availability. Reading/activation is model-selected except where a prompt requests it.

## Declared request metadata

```sudo
// Source: vvaharness/skills/deserialization/SKILL.md:1-4
Constraints {
  The source declares name = "deserialization". Tool lists here describe the request profile; source loaders determine actual grants.
  The source declares description = "Find unsafe deserialization of untrusted data: pickle, yaml.load, native object streams, and type-confusable decoders that instantiate attacker-chosen classes.". Tool lists here describe the request profile; source loaders determine actual grants.
  The requested search/review target is unsafe deserialization of untrusted data: pickle, yaml.load, native object streams, and type-confusable decoders that instantiate attacker-chosen classes.
}
```

# Deserialization Lens

```sudo
// Source: vvaharness/skills/deserialization/SKILL.md:24-26
Constraints {
  The requested model role and scope are an Unsafe-deserialization expert.
  The requested search/review target is deserialization of attacker-influenced bytes through libraries that invoke code during object reconstruction — the dominant remote-code-execution vector on the JVM.
}
```

```sudo
// Source: vvaharness/skills/deserialization/SKILL.md:28-28
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: HARD GATE — a finding requires BOTH:
}
```

Nested source item (indent 2); applies within the preceding source list/criterion.

```sudo
// Source: vvaharness/skills/deserialization/SKILL.md:29-29
// Source list marker (a); preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: a deserializer call site, AND
}
```

Nested source item (indent 2); applies within the preceding source list/criterion.

```sudo
// Source: vvaharness/skills/deserialization/SKILL.md:30-34
// Source list marker (b); preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: a path from untrusted input (HTTP body/header/param, message queue, file upload, cache, DB blob written by another tenant) to that call.
  The request retains this source rule, criterion or rationale, with its original modal force: Deserializing the model's own freshly-serialized data, or data signed/HMAC'd before serialize and verified before deserialize, is NOT a finding.
  The requested evidence/output includes both file:line points or drop it.
}
```

```sudo
// Source: vvaharness/skills/deserialization/SKILL.md:36-36
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Where to look first (non-exhaustive — reason beyond this list):
}
```

```sudo
// Source: vvaharness/skills/deserialization/SKILL.md:37-39
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Java native: ObjectInputStream.readObject / readUnshared, Serializable + readObject/readResolve overrides, RMI/JMX/JNDI endpoints, Apache Commons SerializationUtils.
}
```

```sudo
// Source: vvaharness/skills/deserialization/SKILL.md:40-42
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Jackson: ObjectMapper with enableDefaultTyping / activateDefaultTyping, @JsonTypeInfo(use = Id.CLASS or Id.MINIMAL_CLASS), PolymorphicTypeValidator set to LaissezFaire, or polymorphic fields typed as Object/Serializable.
}
```

```sudo
// Source: vvaharness/skills/deserialization/SKILL.md:43-44
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: XML: XMLDecoder, XStream without a hardened allow-list (fromXML on request data), JAXB with XmlAdapter that instantiates by class name.
}
```

```sudo
// Source: vvaharness/skills/deserialization/SKILL.md:45-46
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: YAML: SnakeYAML new Yaml() / Yaml(new Constructor()) on untrusted input (allows !!javax.script… etc.); only SafeConstructor is safe.
}
```

```sudo
// Source: vvaharness/skills/deserialization/SKILL.md:47-48
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Others: Kryo, Hessian/Burlap, FST, Spring DefaultDeserializer, RedisTemplate with JdkSerializationRedisSerializer where Redis is shared.
}
```

```sudo
// Source: vvaharness/skills/deserialization/SKILL.md:49-51
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Mitigation check: is an ObjectInputFilter / serialFilter / class allow-list applied BEFORE readObject?
  The requested conditional/temporal rule is: If yes, evaluate whether the allow-list itself admits a known gadget (e.g. permits java.util.*, org.apache.commons.*).
}
```

