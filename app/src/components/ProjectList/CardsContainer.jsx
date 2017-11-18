import React from 'react';
import Card from './ProjectsCards';
import './CardsContainer.css';
import projectList from './listOfProjects';

export default class CardsContainer extends React.Component {
  render() {
    return (
      <section id='project-list' className='Container-layout'>
        { projectList.map((item, key) => {
          return (
            <Card
              key={key}
              name={item.name}
              logoLink={item.imageSrc}
              githubLink={item.githubLink}
              description={item.description}
              tag={item.tag}
            />
          );
        })}
      </section>
    );
  }
}
