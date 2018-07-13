import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

// Define the size of the random graph
const xCount = 4;
const yCount = 3;
const boxSize = 350;
const probability = 0.6;

// Figure out the canvas size
const canvasWidth = boxSize * xCount;
const canvasHeight = boxSize * yCount;
const radius = boxSize / 8;

/**
 * GraphView
 */
class GraphView extends Component {
  /**
   * On mount
   */
  componentDidMount() {
    this.updateCanvasConnectedComponents();
  }

  /**
   * On state update
   */
  componentDidUpdate() {
    this.updateCanvasConnectedComponents();
  }

  /**
   * Draw the given verts
   */
  drawVerts(component, color = "blue", clear = true) {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext("2d");
    const vertexes = this.props.graph.vertexes;
    // Clear it
    if (clear) {
      ctx.fillStyle = "white";
      ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    }

    // Draw the edges
    ctx.lineWidth = 2;

    for (let v of component) {
      // From this vert
      v.color = color;
      for (let e of v.edges) {
        // To all these verts
        const v2 = e.destination;
        ctx.beginPath();
        ctx.moveTo(v.pos.x, v.pos.y);
        ctx.lineTo(v2.pos.x, v2.pos.y);
        ctx.strokeStyle = v.color;
        ctx.stroke();
        ctx.closePath();
      }
    }

    // Draw the verts on top
    ctx.strokeStyle = "black";
    for (let v of vertexes) {
      ctx.beginPath();
      ctx.fillStyle = v.color;
      ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI, false);
      ctx.stroke();
      ctx.fill();
    }

    // Draw the vert names
    ctx.font = "14px sans-serif";
    ctx.textAlign = "center";
    ctx.fillStyle = "black";

    for (let v of vertexes) {
      ctx.fillText(v.value, v.pos.x, v.pos.y + 4);
    }
  }

  /**
   * Draw the entire graph
   */
  // updateCanvasEntireGraph() {
  //   const g = this.props.graph;
  //   this.updateCanvasConnectedComponents();
  //   // this.drawVerts(g.vertexes);
  //   //g.dump();
  // }

  /**
   * Draw the connected components
   */
  updateCanvasConnectedComponents() {
    function randomHexColor() {
      let color = ((Math.random() * 240) | 0).toString(16);

      if (color.length === 1) {
        color = "0" + color; // leading zero for values less than 0x10
      }

      return color;
    }

    const g = this.props.graph;
    const connectedComponents = g.getConnectedComponents();

    let clear = true;

    for (let component of connectedComponents) {
      // Color just like in CSS
      const curColor =
        "#" + randomHexColor() + randomHexColor() + randomHexColor();

      this.drawVerts(component, curColor, clear);
      clear = false;
    }
  }

  /**
   * Render
   */
  render() {
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />;
  }
}

/**
 * App
 */
class App extends Component {
  constructor(props) {
    super(props);
    this.onButton = this.onButton.bind(this);

    this.state = {
      graph: new Graph()
    };

    this.state.graph.randomize(xCount, yCount, boxSize, probability);
  }

  /**
   * Handle the button press
   */
  onButton() {
    const state = {
      graph: new Graph()
    };

    state.graph.randomize(xCount, yCount, boxSize, probability);

    this.setState(state);
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
        <button onClick={this.onButton}>Random</button>
      </div>
    );
  }
}

export default App;
