Write a function called
      permutor(text, permutation)
that outputs a reordering of a string of characters.

permutor(‘Hello’,[2,0,3,1,4])

‘lHleo’
      
permutor(‘lHleo’,[1,3,0,2,4])

‘Hello’


Hint, you don’t need very many lines of code for this.  
If you get to more than 8, you are probably being too complicated.  
Ask for some hints, share some code.   
Let’s *do* something! :slightly_smiling_face: (edited) 

After you have done that, you can implement a function called:  
    decoder(permutation):    

This function can derive the decoding permutation for the specified permutation.
The decoding permutation can be used to restore the permuted text to the original.  (the undo)
