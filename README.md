
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

-----------------------------------------------------------------------------------------------------

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

-----------------------------------------------------------------------------------------------------

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
- __Interface base:__  

|  | b1 | b2 | b3 |
|-|:-:|:-:|:-:|
| C1: Array value | Contains null value in some position | All value in the array is int | Empty array |  


- __Valid values:__  
c1b1, c1b2, c1b3  

- __Functional base: PWC__  

|  | b1 | b2 |
|-|:-:|:-:|
| T1: New data is appended correctly | True | False |
| T2: Return false if new data contains int.MIN_VALUE | True | False |
| T3: Shift if array is full | True | False |  

[T1b1, T2b1], [T1b1, T2b2], [T1b2, T2b1], [T1b2, T2b2],  
[T2b1, T3b1], [T2b1, T3b2], [T2b2, T3b1], [T2b2, T3b2]

- __Eliminate redundant tests and infeasible tests:__  
[T1b1, T2b1, T3b2], [T1b1, T2b2, T3b2]  

-__Derived test values:__  

|  | Value | Expected |
|-|:-:|:-:|
| T1: Array contains null value | [1,null] | NullPointer Exception |
| T2: All array elements are int | [1,2] | true |
| T3: null array | [] | NullPointer Exception |
| T4: Array element contains int.MIN_VALUE | [int.min_value] | false |
| T5: arbitrary array input | [1,2] | true |  

-----------------------------------------------------------------------------------------------------

__Method 4:__ testResetBuffer() 
- __Goal:__ Reset the main array to its initial state.
- __Testable Function:__
  - ResetBuffer()
- __Parameters (Not directly):__
  - data [][]
- __Return type:__
  - -
- __Return Value:__
  - -  
- __Exceptional behavior__  
  - -
- __Interface base:__  

|  | b1 | b2 |
|-|:-:|:-:|
| C1: Array element value | All valid (a1) | Contain null value (a2) |
| C2: Array is empty | True | False |  

- __ACoC:__  
[a1, T], [a1, F], [a2, T], [a2, T]  

- __Valid values:__  
[a1, F], [a2, F]  

- __Functional base:__  

|  | b1 | b2 |
|-|:-:|:-:|
| C1: Array element after reset | All default value (-2147483648) | Contain Invalid value |  

- __ACoC:__  
[b1], [b2]   

- __Valid values:__  
[b1]  

-__Derived test values:__  

|  | Array | Expected |
|-|:-:|:-:|
| T1: Array is reset successfully  | [1, 5, 3, 6, 8, ...] | [-2147483648, -2147483648, -2147483648, ...] |
| T2: Array cannot reset | [1, 3, 5, 4, null, ...] | NullPointer Exception |  




-----------------------------------------------------------------------------------------------------

__Method 5:__ TestsetDataRow()
- __Goal:__ To set data in column of the main array.
- __Testable Function:__
  - setDataRow()  
- __Parameters:__
  - int column, array data
- __Return type:__
  - Boolean
- __Return Value:__
  - True    
- __Interface base BCC:__  
Base = (A2,B3)  

|  | b1 | b2 | b3 | b4 |
|-|:-:|:-:|:-:|:-:|
| C1: rowvalue | Null(A1) | Positive(A2) | Zero(A3) | Negative(A4) |
| C2: data array value | Empty(B1) | Contain some null values(B2) | All values are valid (B3) |  |  

T1: (A2,B3)  
T2: (A1,B3)   
T3: (A4,B3)   
T4: (A2,B1)   
T5: (A2,B2)   
T6: (A3,B3)  

- __Eliminate redundant tests and infeasible tests:__  
- __Interface base:__  
(A2,B3),(A3,B3), (A1,B3)  
- __Functional base:__  
(A1), (A2)  
- __BCC Functional base:__  
Base choice = (A1)  

|  | b1 | b2 |
|-|:-:|:-:|
| C1: Data is changed completely | Yes(A1) | No(A2) |  

T1: (A1)  
T2: (A2)  
- __Derived test values__  

|  | Value | Expected |
|-|:-:|:-:|
| T1: Input row value is positive and all values are valid in data array | setDataRow(1,data) | true |
| T2:Input row value is zero and all values are valid in the data array. | setDataRow(0,data) | true |
| T3: Input row value is null and all values are valid in the data array. | setDataRow(null ,data) | NullPointer Exception |
| T4: Data is changed completely | setDataRow(0,data) | true |
| T5: Data is not changed completely | setDataRow(0,null) | NullPointer Exception |  

T1: (A1,B1)   
T2: (A1,B2)   
T3: (A2,B1)  

-----------------------------------------------------------------------------------------------------

  
  




