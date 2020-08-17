const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#0c1d21", /* black   */
  [1] = "#3d94a9", /* red     */
  [2] = "#3571aa", /* green   */
  [3] = "#667daa", /* yellow  */
  [4] = "#848aa9", /* blue    */
  [5] = "#a096a4", /* magenta */
  [6] = "#aa7a82", /* cyan    */
  [7] = "#c2c6c7", /* white   */

  /* 8 bright colors */
  [8]  = "#485558",  /* black   */
  [9]  = "#3d94a9",  /* red     */
  [10] = "#3571aa", /* green   */
  [11] = "#667daa", /* yellow  */
  [12] = "#848aa9", /* blue    */
  [13] = "#a096a4", /* magenta */
  [14] = "#aa7a82", /* cyan    */
  [15] = "#c2c6c7", /* white   */

  /* special colors */
  [256] = "#0c1d21", /* background */
  [257] = "#c2c6c7", /* foreground */
  [258] = "#c2c6c7",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
