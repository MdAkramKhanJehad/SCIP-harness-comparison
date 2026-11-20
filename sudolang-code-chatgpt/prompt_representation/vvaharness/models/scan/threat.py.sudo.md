# vvaharness/models/scan/threat.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## surface_files — source lines 94–99

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/scan/threat.py:94-99
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Every repo-relative file path (from the FILE INVENTORY / entry points / modules lists the model were given) that implements or is reachable from this threat's surface.
  The request retains this source rule, criterion or rationale, with its original modal force: Required whenever the surface names concrete code, not just a general property of the system — this is how the threat reaches the files it affects; an empty list means no downstream stage can act on it.
}
```

## lines — source lines 141–141

Source context: callable `to_prompt_block`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/scan/threat.py:141-141
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: THREAT MODEL:
}
```

## lines — source lines 141–141

Source context: callable `to_prompt_block`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/scan/threat.py:141-141
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: System context:
}
```

## lines — source lines 170–170

Source context: callable `to_compact_prompt_block`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/scan/threat.py:170-170
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: THREAT MODEL:
}
```

## lines — source lines 172–172

Source context: callable `to_compact_prompt_block`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/scan/threat.py:172-172
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: System context:
}
```

## to_prompt_block — source lines 143–143

Source context: callable `to_prompt_block`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(self.assets); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/threat.py:143-143
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Assets ([dynamic source value: len(self.assets); conversion=none; format_spec=none]):
}
```

## to_prompt_block — source lines 148–148

Source context: callable `to_prompt_block`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(self.trust_boundaries); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/threat.py:148-148
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Trust boundaries ([dynamic source value: len(self.trust_boundaries); conversion=none; format_spec=none]):
}
```

## to_prompt_block — source lines 154–154

Source context: callable `to_prompt_block`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(self.threats); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/threat.py:154-154
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Ranked threats ([dynamic source value: len(self.threats); conversion=none; format_spec=none]):
}
```

## to_compact_prompt_block — source lines 178–178

Source context: callable `to_compact_prompt_block`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(assets); conversion=none; format_spec=none`
- `len(self.assets); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/threat.py:178-178
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Assets ([dynamic source value: len(assets); conversion=none; format_spec=none]/[dynamic source value: len(self.assets); conversion=none; format_spec=none]):
}
```

## to_compact_prompt_block — source lines 186–186

Source context: callable `to_compact_prompt_block`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(bounds); conversion=none; format_spec=none`
- `len(self.trust_boundaries); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/threat.py:186-186
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Trust boundaries ([dynamic source value: len(bounds); conversion=none; format_spec=none]/[dynamic source value: len(self.trust_boundaries); conversion=none; format_spec=none]):
}
```

## to_compact_prompt_block — source lines 195–195

Source context: callable `to_compact_prompt_block`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(threats); conversion=none; format_spec=none`
- `len(self.threats); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/threat.py:195-195
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Ranked threats ([dynamic source value: len(threats); conversion=none; format_spec=none]/[dynamic source value: len(self.threats); conversion=none; format_spec=none]):
}
```

## to_prompt_block — source lines 145–145

Source context: callable `to_prompt_block`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `a.sensitivity; conversion=none; format_spec=none`
- `a.name; conversion=none; format_spec=none`
- `a.description; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/threat.py:145-145
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [[dynamic source value: a.sensitivity; conversion=none; format_spec=none]] [dynamic source value: a.name; conversion=none; format_spec=none] — [dynamic source value: a.description; conversion=none; format_spec=none]
}
```

## to_prompt_block — source lines 151–151

Source context: callable `to_prompt_block`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `b.entry_point; conversion=none; format_spec=none`
- `b.crossing; conversion=none; format_spec=none`
- `ra; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/threat.py:151-151
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: b.entry_point; conversion=none; format_spec=none]: [dynamic source value: b.crossing; conversion=none; format_spec=none] → assets: [dynamic source value: ra; conversion=none; format_spec=none]
}
```

## to_compact_prompt_block — source lines 180–180

Source context: callable `to_compact_prompt_block`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `a.sensitivity; conversion=none; format_spec=none`
- `a.name; conversion=none; format_spec=none`
- `a.description; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/threat.py:180-180
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [[dynamic source value: a.sensitivity; conversion=none; format_spec=none]] [dynamic source value: a.name; conversion=none; format_spec=none] — [dynamic source value: a.description; conversion=none; format_spec=none]
}
```

## to_compact_prompt_block — source lines 189–189

Source context: callable `to_compact_prompt_block`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `b.entry_point; conversion=none; format_spec=none`
- `b.crossing; conversion=none; format_spec=none`
- `ra; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/threat.py:189-189
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: b.entry_point; conversion=none; format_spec=none]: [dynamic source value: b.crossing; conversion=none; format_spec=none] → assets: [dynamic source value: ra; conversion=none; format_spec=none]
}
```

## to_prompt_block — source lines 157–158

Source context: callable `to_prompt_block`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `t.id; conversion=none; format_spec=none`
- `t.impact; conversion=none; format_spec=none`
- `t.likelihood; conversion=none; format_spec=none`
- `t.threat; conversion=none; format_spec=none`
- `t.actor; conversion=none; format_spec=none`
- `t.surface; conversion=none; format_spec=none`
- `t.asset; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/threat.py:157-158
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: t.id; conversion=none; format_spec=none] [[dynamic source value: t.impact; conversion=none; format_spec=none]/[dynamic source value: t.likelihood; conversion=none; format_spec=none]] [dynamic source value: t.threat; conversion=none; format_spec=none] (actor=[dynamic source value: t.actor; conversion=none; format_spec=none], surface=[dynamic source value: t.surface; conversion=none; format_spec=none], asset=[dynamic source value: t.asset; conversion=none; format_spec=none]
}
```

## to_compact_prompt_block — source lines 198–199

Source context: callable `to_compact_prompt_block`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `t.id; conversion=none; format_spec=none`
- `t.impact; conversion=none; format_spec=none`
- `t.likelihood; conversion=none; format_spec=none`
- `t.threat; conversion=none; format_spec=none`
- `t.actor; conversion=none; format_spec=none`
- `t.surface; conversion=none; format_spec=none`
- `t.asset; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/threat.py:198-199
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: t.id; conversion=none; format_spec=none] [[dynamic source value: t.impact; conversion=none; format_spec=none]/[dynamic source value: t.likelihood; conversion=none; format_spec=none]] [dynamic source value: t.threat; conversion=none; format_spec=none] (actor=[dynamic source value: t.actor; conversion=none; format_spec=none], surface=[dynamic source value: t.surface; conversion=none; format_spec=none], asset=[dynamic source value: t.asset; conversion=none; format_spec=none]
}
```

## to_prompt_block — source lines 159–159

Source context: callable `to_prompt_block`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `t.controls; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/threat.py:159-159
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: , controls: [dynamic source value: t.controls; conversion=none; format_spec=none]
}
```

## to_compact_prompt_block — source lines 200–200

Source context: callable `to_compact_prompt_block`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `t.controls; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/threat.py:200-200
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: , controls: [dynamic source value: t.controls; conversion=none; format_spec=none]
}
```

