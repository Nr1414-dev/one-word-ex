# One Word From Your Ex

[![make.fun](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![rank](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/Nr1414-dev/one-word-ex/rank.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![reward](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/Nr1414-dev/one-word-ex/reward.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)

Entry for the [One Word From Your Ex](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2) bounty on [make.fun](https://make.fun/).

## The word

**expired** — one word, seven letters. The word an ex would use to
describe you once the relationship has passed its date: shelf life
over, thrown out, done. It is funny at once (a sell-by date on a
person), painfully true, and instantly understood — everyone has thrown
something expired away. The field is full of almost, forgettable,
unavailable and rebound; nobody reached for the expiry date.

## How it works

`main.py` writes exactly that one word to `/output/entry.txt`
(UTF-8, 1–24 characters, no trailing newline), with mode `0644`
so the grader can read it. The word is validated first (one word,
inside the 1–24 character window) and read back after writing.

```sh
python3 main.py
cat /output/entry.txt   # expired
```

## License

MIT — see [LICENSE](LICENSE).
