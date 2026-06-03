# ⚡ STORM AI — Inference API for AI Agents

Deterministic inference backend on NVIDIA DGX Spark. Not a chatbot — purpose-built for agent developers who need reliable, structured output.

**[api.stormengine.cloud](https://api.stormengine.cloud)**

## Why STORM

Most inference APIs are optimized for chat. STORM is optimized for agents — the kind of workload where a single malformed JSON response breaks your pipeline and you don't find out until 20 turns later.

- **Zero structured errors** in 2,859 code-generation tests (EvalScope + vLLM)
- **15-20% less redundant output** vs cloud models — agents run leaner
- **DGX Spark 128GB ARM64** — dedicated hardware, consistent performance
- **Qwen2.5-32B-AWQ** — 64K context, tuned for code + JSON

## Benchmark Summary

| Metric | STORM (DGX) | Mac M4 (14B) |
|--------|------------|-------------|
| Safe concurrency | 30 | 18 |
| Streaming t/s @30 | 307 | — |
| Success rate @30 | 100% | — |
| Code correctness | 2,859/2,859 | — |
| Avg output length | 15-20% leaner | — |

Full report: [bench_report.html](https://api.stormengine.cloud/static/bench_report.html)

## Quick Start

```bash
curl https://api.stormengine.cloud/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "storm-qwen32b",
    "messages": [{"role": "user", "content": "Write a Python function to merge two sorted lists"}],
    "temperature": 0.1
  }'
```

## Pricing

Pay for what you use. No hidden minimums.

| Tier | Price | Limit |
|------|-------|-------|
| Free | $0 | 100 req/day |
| Starter | ¥9.9/mo | 5K req/mo |
| Developer | $49/mo | 50K req/mo |
| Pro | $159/mo | 200K req/mo |

¥0.5 per million tokens beyond quota.

## Ideal For

- **Agent frameworks** — LangChain, CrewAI, AutoGPT backends
- **Code generation** — CI/CD pipelines, automated PR reviews
- **Structured output** — JSON APIs, data extraction, schema validation
- **Deterministic workloads** — where "mostly correct" isn't good enough

## Not Ideal For

- Chatbots and casual conversation
- Creative writing / storytelling
- Multi-modal (we're text-only)

## License

MIT
