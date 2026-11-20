# vvaharness/remediation_agent/interactive/keys.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/interactive/keys.py.evidence.json`. SHA-256: `b3a3fd3d450e518771cba3afb2e3298730161f78d6ba0f5bb659e485ff24f2c5`.

```sudo
// Source: vvaharness/remediation_agent/interactive/keys.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import sys; preserve alias and import-time effects. Then Evaluate once ('up', 'down', 'enter', 'quit', 'other'); assign in source target order to (UP, DOWN, ENTER, QUIT, OTHER).
// Source: vvaharness/remediation_agent/interactive/keys.py:24-34
// Source signature: decode_key(seq: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn decode_key(seq) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/interactive/keys.py:25-25
  In source order: Retain source documentation literal source_literal_25_4; it is not a model call.
  // Source: vvaharness/remediation_agent/interactive/keys.py:26-27
  if (the source predicate seq in ('\x1b[A', '\x1bOA', 'k') is truthy) {
    // Source: vvaharness/remediation_agent/interactive/keys.py:27-27
    End this invocation with UP.
  }
  // Source: vvaharness/remediation_agent/interactive/keys.py:28-29
  if (the source predicate seq in ('\x1b[B', '\x1bOB', 'j') is truthy) {
    // Source: vvaharness/remediation_agent/interactive/keys.py:29-29
    End this invocation with DOWN.
  }
  // Source: vvaharness/remediation_agent/interactive/keys.py:30-31
  if (the source predicate seq in ('\r', source_literal_30_21) is truthy) {
    // Source: vvaharness/remediation_agent/interactive/keys.py:31-31
    End this invocation with ENTER.
  }
  // Source: vvaharness/remediation_agent/interactive/keys.py:32-33
  if (the source predicate seq in ('q', 'Q', '\x1b', '\x03', '\x04') is truthy) {
    // Source: vvaharness/remediation_agent/interactive/keys.py:33-33
    End this invocation with QUIT.
  }
  // Source: vvaharness/remediation_agent/interactive/keys.py:34-34
  End this invocation with OTHER.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/interactive/keys.py:37-63
// Source signature: _read_key() -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _read_key() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/interactive/keys.py:38-38
  In source order: Retain source documentation literal source_literal_38_4; it is not a model call.
  // Source: vvaharness/remediation_agent/interactive/keys.py:39-48
  if (the source predicate sys.platform == 'win32' is truthy) {
    // Source: vvaharness/remediation_agent/interactive/keys.py:40-43
    Perform the following protected operations {
      // Source: vvaharness/remediation_agent/interactive/keys.py:41-41
      In source order: Resolve source import import msvcrt; preserve alias and import-time effects.
    }
    // Source: vvaharness/remediation_agent/interactive/keys.py:42-43
    On the first matching source exception ImportError as e, in handler order {
      // Source: vvaharness/remediation_agent/interactive/keys.py:43-43
      Raise RuntimeError('no raw keyboard input') with explicit source cause e.
    }
    // Source: vvaharness/remediation_agent/interactive/keys.py:44-44
    In source order: Evaluate once msvcrt.getwch(); assign in source target order to ch.
    // Source: vvaharness/remediation_agent/interactive/keys.py:45-47
    if (the source predicate ch in ('\x00', 'à') is truthy) {
      // Source: vvaharness/remediation_agent/interactive/keys.py:46-46
      In source order: Evaluate once msvcrt.getwch(); assign in source target order to ch2.
      // Source: vvaharness/remediation_agent/interactive/keys.py:47-47
      End this invocation with {'H': UP, 'P': DOWN}.get(ch2, OTHER).
    }
    // Source: vvaharness/remediation_agent/interactive/keys.py:48-48
    End this invocation with decode_key(ch).
  }
  // Source: vvaharness/remediation_agent/interactive/keys.py:50-51
  In source order: Resolve source import import termios; preserve alias and import-time effects. Then Resolve source import import tty; preserve alias and import-time effects.
  // Source: vvaharness/remediation_agent/interactive/keys.py:52-53
  if (the source predicate not sys.stdin.isatty() is truthy) {
    // Source: vvaharness/remediation_agent/interactive/keys.py:53-53
    Raise RuntimeError('stdin is not a TTY').
  }
  // Source: vvaharness/remediation_agent/interactive/keys.py:54-55
  In source order: Evaluate once sys.stdin.fileno(); assign in source target order to fd. Then Evaluate once termios.tcgetattr(fd); assign in source target order to old.
  // Source: vvaharness/remediation_agent/interactive/keys.py:56-63
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/interactive/keys.py:57-58
    In source order: Evaluate tty.setraw(fd); retain side effects and discard the expression result. Then Evaluate once sys.stdin.read(1); assign in source target order to ch.
    // Source: vvaharness/remediation_agent/interactive/keys.py:59-60
    if (the source predicate ch == '\x1b' is truthy) {
      // Source: vvaharness/remediation_agent/interactive/keys.py:60-60
      In source order: Apply source augmented assignment ch += sys.stdin.read(2) with source evaluation/in-place semantics.
    }
    // Source: vvaharness/remediation_agent/interactive/keys.py:61-61
    End this invocation with decode_key(ch).
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/remediation_agent/interactive/keys.py:63-63
    In source order: Evaluate termios.tcsetattr(fd, termios.TCSADRAIN, old); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
