######################################################
# author: Devin Anzelmo, devinanzelmo@gmail.com
# licence: FreeBSD

"""
Copyright (c) 2015, Devin Anzelmo
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
 are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
 list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
 this list of conditions and the following disclaimer in the documentation
 and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
 INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
 OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
 OF THE POSSIBILITY OF SUCH DAMAGE.

"""


import pandas as pd
import numpy as np
import functions as fn

model_path = '../models/'
path = '../processed/'
sfx = '_final_subm'
use_xtra_features = '_no_xtra_features'
nt_limit_list = [10, 20, 50, 100, 150, 200, 250, 300]

for nt_limit in nt_limit_list:
    predictions1 = fn.make_prediction1(fn.load_xgb_model(model_path+'bst1_1'+sfx),nt_limit,path)
    predictions2 = fn.make_prediction2(fn.load_xgb_model(model_path+'bst2_1'+sfx),nt_limit,path)
    predictions3 = fn.make_prediction3(fn.load_xgb_model(model_path+'bst3_1'+sfx),nt_limit,path)

    #NOTE set use_xtra_features to False as part of a faster solution
    predictions4 = fn.make_prediction4(fn.load_xgb_model(model_path+'bst4_1'+sfx+use_xtra_features),path,nt_limit,use_xtra_features=False) #change to False for speed up
    predictions5 = fn.make_prediction5(fn.load_xgb_model(model_path+'bst5_1'+sfx+use_xtra_features),path,nt_limit,use_xtra_features=False) #change to False for speed up


    #This is the post processing, the more large values in a subset the more you can subtract
    predictions1 = predictions1 
    predictions2 = predictions2 - 0.0025 
    predictions3 = predictions3 - 0.0024 
    predictions4 = predictions4 - 0.0052 
    predictions5 = predictions5 - 0.0084 


    predictions = pd.concat([predictions1,predictions2,predictions3,predictions4,predictions5])
    predictions = predictions.sort_index()

    subm_columns = ['Predicted'+str(x) for x in range(70)]
    predictions.columns = subm_columns
    predictions.index.name = 'Id'

    predictions.to_csv(f'../output/final_subm_pp_prune_no_xtra_features_{nt_limit}.csv',float_format='%.4f')
    subm_new = pd.read_csv(f'../output/final_subm_pp_prune_no_xtra_features_{nt_limit}.csv',index_col=0)

    #checks that the solution meets the requirements to be properly scored. 
    print(fn.check_solution(subm_new.values))

