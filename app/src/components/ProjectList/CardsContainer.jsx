import React from 'react';
import Card from './ProjectsCards';
import './CardsContainer.css';
import projectList from './listOfProjects';

export default class CardsContainer extends React.Component {
  render() {
    return (
      <div className="Container-layout">
        { projectList.map((item) => {
          return (
            <Card
              name={item.name}
              logoLink={item.imageSrc}
              githubLink={item.githubLink}
              description={item.description}
            />
          );
        })}
      </div>
    );
  }
}
