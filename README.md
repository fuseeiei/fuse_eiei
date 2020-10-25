
__Method 1:__ testInsertData(), testInsertNullData()
- __Goal:__ To test whether the data is inserted into the array
- __Testable Function:__
  - insertData()
- __Parameters:__
  - int value
- __Return type:__
  - int Array
- __Return Value:__
  - int Array with inserted value  
  
  
|  | b1 | b2 |
|-|:-:|:-:|
| C1: int value is null | True | False |
| C2: Input format is int | True | False |
| C3: Occurrence of value in the data array | 0 (c1) | Equal or more than 1 (c2) |

- __PWC__<br/>
[T, T], ~~[T, F]~~, ~~[F, T]~~, [F, F],   
[T, c1], [T, c2], ~~[F, c1]~~, [F, c2],   
[T, c1], ~~[T, c2]~~, [F, c1], [F, c2]

- __Valid values__<br/>
[T, F, c1], [F, T, c2]  

- __Derived test values__

|  | Value | Expected |
|-|:-:|:-:|
| T1: Invalid input | null | NullPointer Exception |
| T2: Valid input | -87 | [.., -87, ..] |  



__Method 2:__ setData()
- __Goal:__ To set the data in the main array
- __Testable Function:__
  - setData()
- __Parameters:__
  - int row, column, data value
- __Return type:__
  - Boolean
- __Return Value:__
  - True, False  
- __ECC Interface base__  

|  | b1 | b2 | b3 | b4 |
|-|:-:|:-:|:-:|:-:|
| C1: Row value | Negative(A1) | Zero(A2) | Positive(A3) | null(A4) |
| C2: column value | Negative(B1) | Zero(B2) | Positive(B3) | null(B4) |
| C3: data value | Negative(C1) | Zero(C2) | Positive(C3) | null(C4) |  

T1: (A1,B1,C1) n  
T2: (A2,B2,C2) y  
T3: (A3,B3,C3) y  
T4: (A4,B4,C4) n  
- __Valid values__  
(A2,B2,C2), (A3,B3,C3)  

- __ECC Functional base__  

|  | b1 | b2 |
|-|:-:|:-:|
| C1: Row value is in range | Yes(A1) | No(A2) |
| C2: column value is in range | Yes(B1) | No(B2) |
| C3: data is set correctly | Yes(C1) | No(C2) |  

T1: (A1,B1,C1) y*  
T2: (A2,B2,C2) n*  

- __Valid values__  
(A1,B1,C1)  
- __Derived test values__  

|  | Value | Expected |
|-|:-:|:-:|
| T1: Row, column, data value value are zero | setData(0, 0, 0) | true |
| T2: Row, column, data value value are positive | setData(1, 1, 1) | true |
| T3: Row, column value is in range and data is set correctly | setData(1, 1, 1) | true |  


__Method 3:__ TestappendDataRow() 
- __Goal:__ To append array input into the back of an existing data array, shift to the right if the existing data array is full.
- __Testable Function:__
  - appendDataRow()
- __Parameters:__
  - int array
- __Return type:__
  - Boolean
- __Return Value:__
  - True, False  
- __Interface base__  

|  | b1 | b2 | b3 |
|-|:-:|:-:|:-:|
| C1: Array value | Contains null value in some position | All value in the array is int | Empty array |  






