# fizzbuzz

Sample repo to showcase [test-splitting on CircleCI](https://circleci.com/docs/parallelism-faster-jobs).

Requires Python 3.10+.
> See [.python-version](.python-version) file.

## Usage

```console

$ PYTHONPATH=src python src/cli.py 15
FIZZBUZZ

$ PYTHONPATH=src python src/cli.py 6
BUZZ

$ PYTHONPATH=src python src/cli.py 100
BUZZ

$ PYTHONPATH=src python src/cli.py 101
101
```
