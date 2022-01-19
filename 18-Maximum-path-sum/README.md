<!-- <style>
    img[alt$=">"] {
      float: right;
    }

    img[alt$="<"] {
      float: left;
      margin-right: 20px;
      margin-bottom: 20px;
    }

    img[alt$="><"] {
      display: block;
      max-width: 100%;
      height: auto;
      margin: auto;
      float: none!important;
    }
    /* This way of work with images in MD, i have found at
    https://stackoverflow.com/questions/255170/markdown-and-image-alignment */

    .red {
      color: red;
    }
    .yellow {
      color: yellow;
    }
    .green {
      color: green;
    }
    .all-content {
      display: flex;
      flex-direction: column;
    }
IT DOESN'T WORK ON GITHUB, SO I COMMENT THIS
</style> -->

# Challenge 18: Maximum path sum

<div class="all-content">

  <div>

  ![generic triangle <](../images/generic-triangle.svg)

  To find the best path, i'll start from bottom to top.

  I can write a generic position <span class="red">i</span> described by a row <span class="red">L</span> (where 'L' is the penultimate line) and a column <span class="red">col</span>.

  The maximum value between L+1[col] and L+1[col + 1] (<span class="red">m</span> and <span class="red">n</span> in the image) will be the best path that passes through <span class="red">i</span>.

  In other words, if a path reached '<span class="red">i</span>', regardless of how, the best option is the maximum between <span class="red">m</span> and <span class="red">n</span>.

  So I can transform my triangle of size <span class="yellow">'n'</span> to a triangle of size <span class="yellow">'n-1'</span> by adding the maximum to the top row.

  To make it clearer, i'll 
  show a numeric example.

  </div>

  <div>

  ![numeric-triangle-1 <](../images/numeric-triangle-1.svg)

  For this example, i'll use a triangle with only 5 lines, resulting in 16 possibilities, wich is very easy to do by brute force, but it's just to show my reasoning.

  In this case, the generic <span class="red">'i'</span> is the number <span class="green">8</span>. Once the path reached it, regardless of the path above, the best option is the maximum value between <span class="green">4</span> and <span class="green">7</span> (<span class="red">m</span> and <span class="red">n</span>).

  So, i'll sum the number <span class="green">7</span> to our <span class="green">8</span> and do this with all of numbers of this line, like showed in the next image

  </div>

  <div>

  ![numeric-triangle-2 <](../images/numeric-triangle-2.svg)

  Here the program must take the numbers in the last line, two by two, and find the maximum between them (Max(x, y)). Then, the programn will sum it to the corresponding number in the penultimate line, and so successively.

  This process is represented by the red triangle:


  <br>

  ![triangle-subtitle ><](../images/triangle-subtitle.svg)

  </div>

  <div>

  ![numeric-triangle-3-5](../images/numeric-triangle-3-5.svg)

  ## The biggest path sum results in 29, regardless of the path taken  
  
  </div>

</div>




