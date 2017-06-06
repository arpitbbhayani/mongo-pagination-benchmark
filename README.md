Mongo Pagination Benchmark
---

This repository contains Python code that benchmarks the [two approaches for implementing pagination in MongoDB](http://arpitbhayani.me)

 - Using `cursor.skip` and `cursor.limit`
 - Using `_id` and `cursor.limit`

## Setup
All required packages are put into requirements.lock file so all you need to
run is the following command
```bash
pip install -r requirements.lock
```

## Execute
```
python main.py
```

The results and analysis are compiled in this [blog post](http://arpitbhayani.me)
