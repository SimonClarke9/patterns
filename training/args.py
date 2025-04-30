#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test( *args, **kwargs):
    """
    Test function to demonstrate the use of *args and **kwargs.
    """
    print("Positional arguments:", args)    
    print("Keyword arguments:", kwargs)

test(1, 2, 3, a=4, b=5)

