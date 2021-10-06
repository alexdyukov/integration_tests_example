# integration\_tests\_example

Example of integration and functional tests with pytest framework,
because most of the internet filled up with unit tests

## Dependencies

Absolute minimum of course is `pytest` python package.
You can fill up all you need by requirements.txt (see `Dockerfile`) or
use raw pip install in your own Dockerfile (see `Dockerfile-raw`).

## How to run

I hope you plan to use this repo as upstream in your own CI,
so look at the example inside docker-compose.yml to build 
Integration Tests stage in pipeline:
1) Run tests:
`docker-compose up -d -p integration_tests_${CI_COMMIT_SHORT_SHA}`
2) Wait until tests done:
`while ! test -f report.html ; do sleep 10; done`
3) Cleanup:
`docker-compose down -p integration_tests_${CI_COMMIT_SHORT_SHA}`
