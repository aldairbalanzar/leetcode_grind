
/* 1a:
- Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.
  - You may choose how to receive the grid input, along with any additional input's that may seem useful
- An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically (not diagionally). You may assume all four edges of the grid are all surrounded by water.
- The following is an example input, and represents 5 islands
grid_1a = [
[1,0,0,1],
[0,1,1,0],
[1,0,0,1],
]

 1b:
- Let's now remove the assumption that all edges of the grid are surrounded by water, and that the grid now "wraps" around both horizontally and vertically. Islands now wrap around the edge, for example the following grid represents 1 island
grid_1b = [
[1,0,0,1],
[0,0,0,1],
[1,0,0,1],
]

You are allowed to change/modify the input. 
*/

const grid_1a = [
    [1,0,0,1],
    [0,1,1,1],
    [1,0,0,1],
  ]
    
  function dfs(i, j) {
  // check if if i and j are in bound
    // check that indeces aren't negative
    if(i < 0 || j < 0){
      return
    }
  
    // check that indeces don't overflow array sizes
    if(i > grid_1a.length - 1 || j > grid_1a[i].length - 1){
      return
    }
  
    // check that value isn't "water (0)"
    if(grid_1a[i][j] === 0) {
      return
    }
  
    // check that value isn't "visited (2)"
    if(grid_1a[i][j] === 2) {
      return
    }
    // mark array[i][j] as visited
    grid_1a[i][j] = 2
    
    // check if neighboring cells are "land (1)" or "water (0) (top, bottom, left, and right)"
    dfs(i+1,j) // bottom
    dfs(i-1,j) // top
    dfs(i, j+1) // right
    dfs(i, j-1) // left
  
    return
  }
  
  // let counter = 0
  // // iterate through L1 array
  // for(let i = 0; i < grid_1a.length; i++) {
  //   // iterate through every L2 array within L1 array
  //   for(let j = 0; j < grid_1a[i].length; j++){
  //     // if array[i][j] value is "land (1)", run it through dfs function
  //     if(grid_1a[i][j] === 1) {
  //       dfs2(i,j)
  //       // increment counter by 1
  //       counter += 1
  //     }
  //   }
  // }
  
  const grid_1b = [
    [1,0,0,1],
    [0,1,0,1],
    [1,0,0,1],
  ]
  
  function dfsWrap(i, j) {
  // check if if i and j are in bound
    // check that indeces aren't negative
    if(i < 0) {
      i = grid_1b.length - 1
    }
    if(j < 0) {
      j = grid_1b[i].length - 1
    }
  
    // check that indeces don't overflow array sizes
    if(i > grid_1b.length - 1) {
      i = 0
    }
    if(j > grid_1b[i].length - 1) {
      j = 0
    }
  
    // check that value isn't "water (0)"
    if(grid_1b[i][j] === 0) {
      return
    }
  
    // check that value isn't "visited (2)"
    if(grid_1b[i][j] === 2) {
      return
    }
    // mark array[i][j] as visited
    grid_1b[i][j] = 2
    
    // check if neighboring cells are "land (1)" or "water (0) (top, bottom, left, and right)"
    dfsWrap(i+1,j) // bottom
    dfsWrap(i-1,j) // top
    dfsWrap(i, j+1) // right
    dfsWrap(i, j-1) // left
  
    return
  }
    
  let counter = 0
  // iterate through L1 array
  for(let i = 0; i < grid_1b.length; i++) {
    // iterate through every L2 array within L1 array
    for(let j = 0; j < grid_1b[i].length; j++){
      // if array[i][j] value is "land (1)", run it through dfs function
      if(grid_1b[i][j] === 1) {
        dfsWrap(i,j)
        // increment counter by 1
        counter += 1
      }
    }
  }
  
  console.log(counter);