'''
How to execute this file:
  python make_label2id.py ./middle_data
'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('output', type=str, 
                    help="Output Path")
args = parser.parse_args()
outputPath = args.output

fileName = '/label2id.pkl'

label2id = {}
## Naver & 창원대 개체명 인식 말뭉치 label
# label_list = ["[PAD]", "-", 
#               "PER_B", "PER_I", "FLD_B", "FLD_I", "AFW_B", "AFW_I", "ORG_B", "ORG_I", "LOC_B", "LOC_I",  
#               "CVL_B", "CVL_I", "DAT_B", "DAT_I", "TIM_B", "TIM_I", "NUM_B", "NUM_I", "EVT_B", "EVT_I", 
#               "ANM_B", "ANM_I", "PLT_B", "PLT_I", "MAT_B", "MAT_I", "TRM_B", "TRM_I", 
#               "X", "[CLS]", "[SEP]"]

## ETRI 개체명 인식 말뭉치 label
label_list = ["[PAD]", "-", 
              "PS_B", "PS_I", "LC_B", "LC_I", "OG_B", "OG_I", "DT_B", "DT_I", "TI_B", "TI_I", 
              "X","[CLS]","[SEP]"]

with open(outputPath + fileName, 'w') as f:
    for (i, label) in enumerate(label_list, 1):
        label2id[label] = i
    
    f.write(str(label2id))
    print('File Saved!')
