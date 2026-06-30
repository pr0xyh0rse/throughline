# Source Verification Pass v0

Date: 2026-05-30

Scope: strongest neighbours from `comparator_source_table_v0.csv`. Direct source pages were fetched with `curl` into `<local_fetch_cache>/`, then parsed locally. This upgrades planning rows from snippet-only to abstract/page-verified where title and abstract/page description were captured.

## Fetch receipt

```text
WritingBench	https://arxiv.org/abs/2503.05244	200	47225	https://arxiv.org/abs/2503.05244
EQ-Bench_Longform_Creative_Writing	https://eqbench.com/creative_writing_longform.html	200	22497	https://eqbench.com/creative_writing_longform.html
ConStory-Bench	https://arxiv.org/abs/2603.05890	200	46592	https://arxiv.org/abs/2603.05890
LongGenBench	https://arxiv.org/abs/2409.02076	200	46041	https://arxiv.org/abs/2409.02076
Towards_A_Novel_Benchmark	https://aclanthology.org/2025.findings-acl.1114/	200	39433	https://aclanthology.org/2025.findings-acl.1114/
NoCha_One_Thousand_and_One_Pairs	https://arxiv.org/abs/2406.16264	200	47600	https://arxiv.org/abs/2406.16264
RoleLLM	https://aclanthology.org/2024.findings-acl.878/	200	46090	https://aclanthology.org/2024.findings-acl.878/
CharacterBox	https://arxiv.org/abs/2412.05631	200	47596	https://arxiv.org/abs/2412.05631
IFEval	https://arxiv.org/abs/2311.07911	200	46768	https://arxiv.org/abs/2311.07911
RewriteLM_OpenRewriteEval	https://arxiv.org/abs/2305.15685	200	47149	https://arxiv.org/abs/2305.15685

```

## Verified neighbours

### WritingBench

- Status: `abstract_verified` via `arxiv_abs`

- URL: https://arxiv.org/abs/2503.05244

- arXiv ID: `2503.05244`

- Title: WritingBench: A Comprehensive Benchmark for Generative Writing

- Authors: Wu, Yuning, Mei, Jiahao, Yan, Ming, Li, Chenliang, Lai, Shaopeng, Ren, Yuran, Wang, Zijia, Zhang, Ji, Wu, Mengyue, Jin, Qin

- Date: 2025/03/07

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### EQ-Bench Longform Creative Writing

- Status: `source_page_verified` via `benchmark_page`

- URL: https://eqbench.com/creative_writing_longform.html

- Title: EQ-Bench Longform Creative Writing Leaderboard

- Year: 2025

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### ConStory-Bench

- Status: `abstract_verified` via `arxiv_abs`

- URL: https://arxiv.org/abs/2603.05890

- arXiv ID: `2603.05890`

- Title: Lost in Stories: Consistency Bugs in Long Story Generation by LLMs

- Authors: Li, Junjie, Guo, Xinrui, Wu, Yuhao, Lee, Roy Ka-Wei, Li, Hongzhi, Xie, Yutao

- Date: 2026/03/06

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### LongGenBench

- Status: `abstract_verified` via `arxiv_abs`

- URL: https://arxiv.org/abs/2409.02076

- arXiv ID: `2409.02076`

- Title: LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs

- Authors: Wu, Yuhao, Hee, Ming Shan, Hu, Zhiqing, Lee, Roy Ka-Wei

- Date: 2024/09/03

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### Towards A “Novel” Benchmark

- Status: `abstract_verified` via `acl_anthology`

- URL: https://aclanthology.org/2025.findings-acl.1114/

- Title: Towards A “Novel” Benchmark: Evaluating Literary Fiction with Large Language Models

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### NoCha / One Thousand and One Pairs

- Status: `abstract_verified` via `arxiv_abs`

- URL: https://arxiv.org/abs/2406.16264

- arXiv ID: `2406.16264`

- Title: One Thousand and One Pairs: A "novel" challenge for long-context language models

- Authors: Karpinska, Marzena, Thai, Katherine, Lo, Kyle, Goyal, Tanya, Iyyer, Mohit

- Date: 2024/06/24

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### RoleLLM

- Status: `abstract_verified` via `acl_anthology`

- URL: https://aclanthology.org/2024.findings-acl.878/

- Title: RoleLLM: Benchmarking, Eliciting, and Enhancing Role-Playing Abilities of Large Language Models

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### CharacterBox

- Status: `abstract_verified` via `arxiv_abs`

- URL: https://arxiv.org/abs/2412.05631

- arXiv ID: `2412.05631`

- Title: CharacterBox: Evaluating the Role-Playing Capabilities of LLMs in Text-Based Virtual Worlds

- Authors: Wang, Lei, Lian, Jianxun, Huang, Yi, Dai, Yanqi, Li, Haoxuan, Chen, Xu, Xie, Xing, Wen, Ji-Rong

- Date: 2024/12/07

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### IFEval

- Status: `abstract_verified` via `arxiv_abs`

- URL: https://arxiv.org/abs/2311.07911

- arXiv ID: `2311.07911`

- Title: Instruction-Following Evaluation for Large Language Models

- Authors: Zhou, Jeffrey, Lu, Tianjian, Mishra, Swaroop, Brahma, Siddhartha, Basu, Sujoy, Luan, Yi, Zhou, Denny, Hou, Le

- Date: 2023/11/14

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### RewriteLM / OpenRewriteEval

- Status: `abstract_verified` via `arxiv_abs`

- URL: https://arxiv.org/abs/2305.15685

- arXiv ID: `2305.15685`

- Title: RewriteLM: An Instruction-Tuned Large Language Model for Text Rewriting

- Authors: Shu, Lei, Luo, Liangchen, Hoskere, Jayakumar, Zhu, Yun, Liu, Yinxiao, Tong, Simon, Chen, Jindong, Meng, Lei

- Date: 2023/05/25

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


## Brake

`abstract_verified` means the source page and abstract/page description were directly fetched and parsed. It does **not** mean full methodology has been read. `source_page_verified` is weaker: the benchmark page exists and page-level method text was captured, but it is not an academic abstract. Upgrade to `paper_verified` only after a full enough paper read to support detailed claims.

## Additional source verification pass v0b

```text
NarrativeQA	https://github.com/google-deepmind/narrativeqa	200	269414	https://github.com/google-deepmind/narrativeqa
NovelQA	https://arxiv.org/abs/2403.12766	200	47678	https://arxiv.org/abs/2403.12766
LongBench	https://arxiv.org/abs/2308.14508	200	48905	https://arxiv.org/abs/2308.14508
RULER	https://arxiv.org/abs/2404.06654	200	47707	https://arxiv.org/abs/2404.06654
CharacterEval	https://arxiv.org/abs/2401.01275	200	46127	https://arxiv.org/abs/2401.01275
BigToM	https://arxiv.org/abs/2306.15448	200	46643	https://arxiv.org/abs/2306.15448
SWE-bench_Verified	https://openai.com/index/introducing-swe-bench-verified/	403	9769	https://openai.com/index/introducing-swe-bench-verified/
tau-bench	https://arxiv.org/abs/2406.12045	200	45019	https://arxiv.org/abs/2406.12045
BFCL	https://gorilla.cs.berkeley.edu/leaderboard.html	200	16207	https://gorilla.cs.berkeley.edu/leaderboard.html
GAIA	https://arxiv.org/abs/2311.12983	200	45702	https://arxiv.org/abs/2311.12983

```

### NarrativeQA
- Status: `source_page_verified` via `github_repo`
- URL: https://github.com/google-deepmind/narrativeqa

- Title: GitHub - google-deepmind/narrativeqa: This repository contains the NarrativeQA dataset. It includes the list of documents with Wikipedia summaries, links to full stories, and questions and answers.

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### NovelQA
- Status: `abstract_verified` via `arxiv_abs`
- URL: https://arxiv.org/abs/2403.12766

- arXiv ID: `2403.12766`

- Title: NovelQA: Benchmarking Question Answering on Documents Exceeding 200K Tokens

- Authors: Wang, Cunxiang, Ning, Ruoxi, Pan, Boqi, Wu, Tonghui, Guo, Qipeng, Deng, Cheng, Bao, Guangsheng, Hu, Xiangkun

- Date: 2024/03/18

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### LongBench
- Status: `abstract_verified` via `arxiv_abs`
- URL: https://arxiv.org/abs/2308.14508

- arXiv ID: `2308.14508`

- Title: LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding

- Authors: Bai, Yushi, Lv, Xin, Zhang, Jiajie, Lyu, Hongchang, Tang, Jiankai, Huang, Zhidian, Du, Zhengxiao, Liu, Xiao

- Date: 2023/08/28

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### RULER
- Status: `abstract_verified` via `arxiv_abs`
- URL: https://arxiv.org/abs/2404.06654

- arXiv ID: `2404.06654`

- Title: RULER: What's the Real Context Size of Your Long-Context Language Models?

- Authors: Hsieh, Cheng-Ping, Sun, Simeng, Kriman, Samuel, Acharya, Shantanu, Rekesh, Dima, Jia, Fei, Zhang, Yang, Ginsburg, Boris

- Date: 2024/04/09

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### CharacterEval
- Status: `abstract_verified` via `arxiv_abs`
- URL: https://arxiv.org/abs/2401.01275

- arXiv ID: `2401.01275`

- Title: CharacterEval: A Chinese Benchmark for Role-Playing Conversational Agent Evaluation

- Authors: Tu, Quan, Fan, Shilong, Tian, Zihang, Yan, Rui

- Date: 2024/01/02

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### BigToM
- Status: `abstract_verified` via `arxiv_abs`
- URL: https://arxiv.org/abs/2306.15448

- arXiv ID: `2306.15448`

- Title: Understanding Social Reasoning in Language Models with Language Models

- Authors: Gandhi, Kanishk, Fränken, Jan-Philipp, Gerstenberg, Tobias, Goodman, Noah D.

- Date: 2023/06/21

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### SWE-bench Verified
- Status: `fetch_blocked_403` via `blocked_web_page`
- URL: https://openai.com/index/introducing-swe-bench-verified/

- Title: not captured

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### tau-bench
- Status: `abstract_verified` via `arxiv_abs`
- URL: https://arxiv.org/abs/2406.12045

- arXiv ID: `2406.12045`

- Title: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

- Authors: Yao, Shunyu, Shinn, Noah, Razavi, Pedram, Narasimhan, Karthik

- Date: 2024/06/17

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### Berkeley Function Calling Leaderboard / BFCL
- Status: `source_page_verified` via `benchmark_page`
- URL: https://gorilla.cs.berkeley.edu/leaderboard.html

- Title: Berkeley Function Calling Leaderboard (BFCL) V4

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### GAIA
- Status: `abstract_verified` via `arxiv_abs`
- URL: https://arxiv.org/abs/2311.12983

- arXiv ID: `2311.12983`

- Title: GAIA: a benchmark for General AI Assistants

- Authors: Mialon, Grégoire, Fourrier, Clémentine, Swift, Craig, Wolf, Thomas, LeCun, Yann, Scialom, Thomas

- Date: 2023/11/21

- Abstract/page note: Omitted in public preview; see source URL/DOI for the original abstract.


### SWE-bench Verified alternate source
- Status: `source_page_verified` via `benchmark_page`
- URL: https://www.swebench.com/
- Title: SWE-bench Leaderboards
- Page note: SWE-bench Verified is a human-filtered subset of 500 instances; use the Agent dropdown to compare LMs with mini-SWE-agent or view all agents [ Post ]. SWE-bench Multilingual features 300 tasks across 9 programming languages [ Post ]. SWE-bench Lite is a subset curated for less costly evaluation [ Post ]. SWE-bench Multimodal features issues with visual elements [ Post ]. Each entry reports the % Resolved metric, the percentage of instances solved (out of 2294 Full, 500 Verified, 300 Lite & Multilingual, 517 Multimodal). Analyze Results in Detail News [11/2025] Introducing CodeClash, our new eval of LMs as goal (not task) oriented developers! 

