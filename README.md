# ccf-agent

一个面向 CCF 风格算法章节写作的 agent 项目。目标是把强模型的长思考能力、few-shot、评测 harness、上下文 prompt 和个人写作风格 skill 组合成一套可复用的写作系统。

## 为什么做

我想把“算法章节写得既准确又有作者感”这件事产品化：

- 用强模型承担结构推理和技术展开。
- 用 few-shot 固定章节颗粒度、解释节奏和推导密度。
- 用 context prompt 固定写作任务、读者画像、边界和禁区。
- 用个人写作风格 skill 保留稳定的语气、表达偏好和审美。
- 用 harness 检查章节是否真的覆盖了问题定义、核心思路、复杂度、边界条件和可读性。

## 项目结构

```text
ccf-agent/
  docs/
    vision.md
  examples/
    few-shot/
      algorithm-chapter.md
  harness/
    README.md
    evaluate.py
  prompts/
    algorithm-chapter.md
    context.md
  skills/
    personal-writing-style.md
  .gitignore
  README.md
```

## 快速开始

先生成一个章节草稿：

```powershell
python harness/evaluate.py examples/few-shot/algorithm-chapter.md
```

当前 harness 先做结构和关键词检查，后续可以接入模型评审、回归样例和多维打分。

## Agent 配方

基础组合：

1. `prompts/context.md`：全局任务、读者、输出边界。
2. `prompts/algorithm-chapter.md`：单章生成指令。
3. `skills/personal-writing-style.md`：个人写作风格约束。
4. `examples/few-shot/algorithm-chapter.md`：目标章节样例。
5. `harness/evaluate.py`：输出质量检查。

## Roadmap

- [ ] 增加真实 CCF 算法章节样例集。
- [ ] 支持从题面自动提取问题定义、约束和算法标签。
- [ ] 增加章节质量评分：正确性、完整性、推导清晰度、风格一致性。
- [ ] 支持多模型生成和交叉评审。
- [ ] 增加 CLI：`ccf-agent draft`、`ccf-agent review`、`ccf-agent polish`。

