import './Business_Segment.css';
import ImageCarousel from "./ImageCarousel";


import React, { Component } from 'react'

export default class BusinessSegment extends Component {
  render() {
    return (
      <div className="businessSegmentContainer">
  
     <div className="textBusinessSegmentHeading">
      <h1 className="headingBusinessSegment">Explore your business segment</h1>
      <p className="textBusinessSegment">Providing support to diverse set of business segments</p>
     </div>
      <ImageCarousel/> 
</div>
    )
  }
}



