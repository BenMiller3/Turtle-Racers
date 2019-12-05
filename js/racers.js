let greenTurtleImg;
let redTurtleImg;
let yellowTurtleImg;
let blueTurtleImg;
let purpleTurtleImg;

let raceIsOn = false;
let standings = [];

class Turtle {

    constructor(ypos, image, name)
    {
        this.ypos = ypos;
        this.image = image;
        this.xpos = 0;
        this.xspeed = 2.2;
        this.topSpeed = 2.2;
        this.xdirection = 1;
        this.name = name;
        this.racing = false;
    }

    run() {
        this.xpos = this.xpos + (this.xspeed * this.xdirection * Math.random());

        if (this.xpos > 575){
            if (this.racing)
            {
                standings.push(this.name);
                this.updateStandings();
            }
            this.stop();
        }
        else
        {
            this.racing = true;
        }
    }

    stop() {
        this.xspeed = 0;
        this.racing = false;
    }

    updateStandings() {
        var resultString = "Standings: ";
        
        standings.forEach(element => {
            resultString += element + " ";
        });
        document.getElementById("standings").innerHTML = resultString;
    }

}

function setup() {
    var canvas = createCanvas(640, 480);
    canvas.parent('sketch-holder');

    greenTurtleImg = loadImage('assets/turtle_1.png');
    redTurtleImg = loadImage('assets/turtle-red-1.png');
    yellowTurtleImg = loadImage('assets/turtle-yellow-1.png');
    blueTurtleImg = loadImage('assets/turtle-blue-1.png');
    purpleTurtleImg = loadImage('assets/turtle-purple-1.png');

    GreenTurtle = new Turtle(25, greenTurtleImg, "Green");
    RedTurtle = new Turtle(100, redTurtleImg, "Red");
    YellowTurtle = new Turtle(175, yellowTurtleImg, "Yellow");
    BlueTurtle = new Turtle(250, blueTurtleImg, "Blue");
    PurpleTurtle = new Turtle(325, purpleTurtleImg, "Purple");

    turtles = [GreenTurtle, RedTurtle, YellowTurtle, BlueTurtle, PurpleTurtle];
}

function draw() {
    clear();
    background(250, 250, 250);

    if (raceIsOn) {
        turtles.forEach(element => {
            element.run();
        });
    }

    turtles.forEach(element => {
        image(element.image, element.xpos, element.ypos);
    });
}

function startRace() {
    if (standings.length > 1) {
        resetRace();
    }
    raceIsOn = true;
    standings = [];
    turtles.forEach(element => {
        element.xspeed = element.topSpeed;
    });
}

function resetRace() {

    raceIsOn = false;

    document.getElementById("standings").innerHTML = "Standings: ";

    turtles.forEach(element => {
        element.xpos = 0;
    });

}