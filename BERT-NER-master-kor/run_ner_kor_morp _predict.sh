#!/usr/bin/env bash

  python BERT_NER_morp.py\
    --task_name="NER"  \
    --do_lower_case=False \
    --crf=True \
    --do_train=True   \
    --do_eval=False   \
    --do_predict=True   \
    --data_dir=data/etri   \
    --data_dir=data/etri   \
    --vocab_file=morp/vocab.korean_morp.list  \
    --bert_config_file=morp/bert_config.json \
    --init_checkpoint=morp/model.ckpt   \
    --max_seq_length=128   \
    --train_batch_size=16   \
    --learning_rate=2e-5   \
    --num_train_epochs=4.0   \
    --output_dir=./output/result_dir


# perl conlleval.pl -d '\t' < ./output/result_dir/label_test.txt
