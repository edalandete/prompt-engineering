/* draw a brown wooden boat with a white sail on top of a blue ocean
 - the sky is light blue with one white cloud
 - the cloud has three different sized circles that overlap each other
 - the sun is a yellow circle inside a yellow-orange circle inside an orange circle inside a yellow circle in the top right corner
 - the sail is a large white triangle connected to the top of the dark brown mast down to the tip of the front of the boat
 - the boat is curved at the bottom and has a dark brown rectangle for the body 
*/

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  
  //sky
  fill(173, 216, 230);
  rect(0, 0, 400, 300);
  
  //cloud
  fill(255);
  ellipse(50, 50, 50, 50);
  ellipse(70, 50, 70, 70);
  ellipse(90, 50, 50, 50);
  
  //sun
  fill(255, 165, 0);
  ellipse(350, 50, 100, 100);
  fill(255, 215, 0);
  ellipse(350, 50, 80, 80);
  fill(255, 255, 0);
  ellipse(350, 50, 60, 60);
  fill(255, 255, 0);
  ellipse(350, 50, 40, 40);
  
  //ocean
  fill(0, 0, 255);
  rect(0, 300, 400, 100);
  
  //boat
  fill(139, 69, 19);
  beginShape();
  vertex(100, 300);
  vertex(150, 300);
  vertex(200, 350);
  vertex(50, 350);
  endShape(CLOSE);
  
  //sail
  fill(255);
  beginShape();
  vertex(150, 150);
  vertex(150, 300);
  vertex(200, 300);
  endShape(CLOSE);
  
  //mast
  fill(139, 69, 19);
  rect(150, 150, 10, 150);
}