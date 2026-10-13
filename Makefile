.PHONY: install test run clean

install:
	pip install -r requirements.txt

# Offline, no API key, no network. This is the gate.
test:
	pytest -q

# Generate the policies in profile.example.yaml. Falls back to a deterministic
# draft if no LLM is reachable. Add LLM env vars (see .env.example) to tailor.
run:
	python generate.py --profile profile.example.yaml --out output

# Same, but never contact an LLM.
run-offline:
	python generate.py --profile profile.example.yaml --out output --no-llm

clean:
	rm -f output/*.md output/*.docx
	rm -rf __pycache__ .pytest_cache tests/__pycache__
