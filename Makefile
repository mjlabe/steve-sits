.PHONY: run
run:
	python3 -m http.server --directory ./sit_for_today/html

build:
	sg1 render sit_for_today

syncs3:
	aws s3 sync images/ s3://sitfortoday/