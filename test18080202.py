#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def findMinandMax(L):
	if L!=[]:	
		maxn = L[0]
		minn = L[0]
		for a in L:
			if a > maxn:
				maxn = a
			if a < minn:
				minn = a
		return(minn,maxn)
	else:
		return(None,None)

	
		
