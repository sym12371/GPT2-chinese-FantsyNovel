# GPT2-Chinese-trained-with-FantasyNovel
A GPT2-Chinese Model trained with some fantasy novel
1.Description:
---
训练一个中文GPT2模型，使用BERT的Tokenizer.中文语料采用常见玄幻小说的部分章节。训练15个周期，batchsize=4。最终可以续写10句以上的玄幻苍穹小说。

2.Start:
----
(1)***environment***

首先，我们下载依赖。
```bash
pip install -r requirements.txt
```

(2)***dataset***

准备中文语料，放置在./data/文件夹下
使用convert_text_files.py脚本来处理.txt语料，将其转换为UTF-8编码后输出到一个.json文件中，将每一个txt文件的全部内容清除控制符和非法字符后作为json列表中的一个元素
```bash
python convert_text_files.py
```

(3)***Model***

在model_config 定义初始GPT-2模型的超参数配置，
- "initializer_range": 0.02 ： 定义了模型参数（如权重矩阵）在初始化时的标准差，权重会在均值为0，标准差为0.02的正态分布中进行随机初始化。
- "layer_norm_epsilon": 1e-05 ： 用于层归一化的常数，用于避免在归一化过程中出现除以零的情况。设置值为1e-05，用于稳定训练。
- "n_ctx": 1024 ： 表示模型上下文窗口的大小，GPT-2 在生成文本时会考虑的最大序列长度。最大长度设为1024，即模型一次最多能处理1024个 token。
- "n_embd": 768 ： 表示每个token的嵌入维度大小，即模型中词向量的维度。设置为768，即每个词汇的表示向量是768维的。
- "n_head": 12 ： 表示自注意力机制中的注意力头的数量。设置为12，即模型的多头注意力机制中有12个独立的头。
- "n_layer": 10 ： 表示 Transformer 编码器中的层数。在这里，设置为 12，即模型有 12 层堆叠的 Transformer 块。
- "n_positions": 1024 ： 表示模型可以处理的最大位置索引，即序列中的最大位置数。最大位置数为 1024，和 n_ctx一致，表示模型最多能处理1024个位置的token。
- "vocab_size": 13317 ： 表示词汇表的大小，即模型可以识别和生成的词汇数量。在这里，词汇表大小为 21128，表示该模型可以处理的词汇量为21128个不同的 token。


(4)***Training***

现在，我们可以使用我们处理好的数据集来训练我们的初始gpt2模型，使用如下命令：
```bash
python train.py  --raw_data_path data/train.json --epochs 15 --log_step 100 --stride 512 --output_dir model/ --device 0,1 --num_pieces 50 --raw --batch_size 4
```

在这个过程中，我们可以看到命令窗口打印出模型的config文件，定义了模型的结构；
{
  "attn_pdrop": 0.1,
  "embd_pdrop": 0.1,
  "finetuning_task": null,
  "initializer_range": 0.02,
  "layer_norm_epsilon": 1e-05,
  "n_ctx": 1024,
  "n_embd": 768,
  "n_head": 12,
  "n_layer": 10,
  "n_positions": 1024,
  "num_labels": 1,
  "output_attentions": false,
  "output_hidden_states": false,
  "output_past": true,
  "pruned_heads": {},
  "resid_pdrop": 0.1,
  "summary_activation": null,
  "summary_first_dropout": 0.1,
  "summary_proj_to_labels": true,
  "summary_type": "cls_index",
  "summary_use_proj": true,
  "torchscript": false,
  "use_bfloat16": false,
  "vocab_size": 13317
}

训练过程中，每个epoch对应的模型都将存储在./model/目录下，最终训练好的模型将存储在./model/final_model/路径中。

(5)***Generate***

现在，我们可以使用我们用目标语料训练生成的模型来进行文字生成，使用如下命令：
```bash
python generate.py   --device 1   --length 500   --tokenizer_path cache/vocab_small.txt   --model_path model/final_model   --prefix "[CLS]唐三大喝一声"   --topp 1   --temperature 1.0 --save_samples --save_samples_path ./mnt/  --nsample 5
```

3.Result
--
最终会生成5个文字样本，存储在./mnt/目录下，其中之一如下：

======================================== SAMPLE 1 ========================================

唐三大喝一声，手中黄金三叉戟一横，一道金色光斩而出，直奔唐三撞来。唐三的反应很快，身体半转，手中的海神三叉戟在海神之心上一挑，戟刃向下，黄金十三戟的镰刀上金光大放，化为无数光圈的光轮在这一刹那就被那金色光环笼罩在内。唐三自身已经被震退，左脚尖直飞，海神三叉戟也像是一个金色流星般切断了虚空消失似的，黄金十三戟竟然在半空之中幻化成了一圈夺目的金色光环，化为六点金光将他右臂和左臂的魂力注入其中。轰然巨响之中，唐三的左脚为中心点，左手与海神三叉戟合二为一，一圈金色光环从海神右肩上爆开，直奔那胸铠甲下扑去。与此同时，唐三左臂处那海神之心的海神之力也骤然爆发出来，强烈的金光将他的左腿弹的飞速后缩，同时，他左臂上原本金色的海神八翼完全变成了金色，在那金色的能量作用下，竟然被那强劲爆炸开一条巨大的海神之力硬生生地抽击在一点一点，将那恐怖的能量炸得粉碎。噗的一声，唐三的左腿处，在海神三叉戟爆发的同时，他右手也又飞了出去。海神三叉戟又飞了出去，半空中一个金色光环瞬间破碎，就像是太阳从天而降，化为点金光冲天而起，化为点金色光环直接朝着唐三的身体而去，直奔唐三撞击而来。

==========================================================================================