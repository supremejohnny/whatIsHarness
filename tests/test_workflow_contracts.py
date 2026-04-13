from harness_demo.harness_agent import run_harness


def test_harness_result_has_contract_fields():
    result, steps = run_harness("issues/fixtures/003_fix_and_test_and_schema.md")
    assert result["mode"] == "harness"
    assert result["tests_passed"] is True
    assert any(step["state_to"] == "TESTS_RUN" for step in steps)
