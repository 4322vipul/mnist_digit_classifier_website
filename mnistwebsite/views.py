from django.shortcuts import render,redirect
from .models import given_image,predicted_label,image_name
from .forms import given_image_form
import numpy as np
import pandas as pd
from PIL import Image
import cv2
import os.path
import pickle
from sklearn.tree import DecisionTreeClassifier

# Create your views here.


def home(request):
    form=given_image_form(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        
        a=form.cleaned_data['image_given']
        name=image_name(name_of_image=a)
        name.save()
        
        b=image_name.objects.all().last()
        print(b)
        c=str(b)
        new_path=os.path.join('/home/vipul/media/',c)
        print(new_path)
        
        img=cv2.imread(new_path)
        print(img)
    
        arr=np.array(img)
        print(arr.shape)
        
        new_img=np.reshape(arr,(784,3), order='C')
        final_img=new_img[0:,1]
        print(new_img.shape)
        print(final_img.shape)
        
        #classifier=decision_tree_model()
        #pred_label=classifier.predict([final_img])
        #label_pred=predicted_label(label=np.asscalar(pred_label))
        #label_pred.save()
        
        loaded_classifier=pickle.load(open('decision_tree_model.sav','rb'))
        pred_label=loaded_classifier.predict([final_img])
        label_pred=predicted_label(label=np.asscalar(pred_label))
        label_pred.save()
        
        
        number=predicted_label.objects.all().last()
        context={"number":number}
        
        return render(request,'mnistwebsite/successPage.html',context)
    
    context={'form':form}
    return render(request,'mnistwebsite/home.html',context)
    
def successPage(request):
    
    return render(request,'successPage.html')

