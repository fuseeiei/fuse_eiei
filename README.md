# 
__Method 1:__ testInsertData(), testInsertNullData()
* __Goal:__ To test whether the data is inserted into the array
* __Testable Function:__
  * insertData()
* __Parameters:__
  * int value
* __Return type:__
  * int Array
* __Return Value:__
  * int Array with inserted value
<br>  
|  | b1 | b2 |
|-|:-:|:-:|
| C1: int value is null | True | False |
| C2: Input format is int | True | False |
| C3: Occurrence of value in the data array | 0 (c1) | Equal or more than 1 (c2) |
</br>
__PWC:___
[T, T], [T, F], [F, T], [F, F], 
[T, c1], [T, c2], [F, c1], [F, c2], 
[T, c1], [T, c2], [F, c1], [F, c2]
