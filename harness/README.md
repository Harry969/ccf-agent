# Harness

这里放用于检查 agent 输出质量的脚本。

当前版本的 `evaluate.py` 是一个轻量结构检查器。它不会判断算法一定正确，但可以快速发现章节缺少关键组成部分。

## 使用

```powershell
python harness/evaluate.py path\to\chapter.md
```

## 后续方向

- 接入 LLM-as-judge，对正确性、风格和完整性打分。
- 对同一题目保存多次生成结果，做回归比较。
- 检查章节是否引用了不存在的题面条件。
- 检查复杂度变量是否和题面一致。

