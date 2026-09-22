# AI Release Risk Analyzer

An AI-assisted engineering tool that analyzes pull requests and identifies potential release risks.

## Problem

Large software changes can introduce production risk through:

- Large code changes
- Critical system modifications
- Database migrations
- Missing test coverage
- High-risk infrastructure changes

Traditional code review can miss combinations of these signals.

## Architecture

GitHub Pull Request
        |
        v
PR Analyzer
        |
        v
Risk Signal Extraction
        |
        v
Deterministic Risk Engine
        |
        v
Risk Score
        |
        v
Local LLM
        |
        v
AI Risk Assessment
        |
        v
Engineering Recommendation

## Design Principle

The system separates deterministic risk detection from AI reasoning.

Deterministic logic provides:

- Explainability
- Repeatability
- Testability
- Predictable behavior

The LLM provides:

- Contextual analysis
- Risk explanation
- Recommended validation
- Deployment strategy suggestions

## Current Features

- Pull request metadata analysis
- Critical file detection
- Database migration detection
- Test-change detection
- Deterministic risk scoring
- Local LLM assessment
- Automated engineering recommendations

## Technology

- Python
- Ollama
- Qwen
- Pytest

## Example

Input:

Migration of authentication sessions to a new cache.

Output:

Risk Level: HIGH

Risk factors:

- Large code change
- Authentication code modified
- Database migration detected

AI recommendations:

- Additional integration testing
- Canary deployment
- Increased monitoring after deployment

## Future Architecture

The project will evolve toward:

GitHub App
    |
    v
Webhook
    |
    v
PR Analysis Service
    |
    +---- Static Analysis
    |
    +---- Test Analysis
    |
    +---- Dependency Analysis
    |
    +---- Historical Incidents
    |
    v
Risk Engine
    |
    v
LLM
    |
    v
GitHub PR Comment

## Future Improvements

- GitHub App integration
- Historical incident data
- Code ownership
- Dependency risk analysis
- Test coverage analysis
- Deployment risk
- Structured LLM output
- Risk evaluation dataset
- OpenTelemetry
- CI/CD integration