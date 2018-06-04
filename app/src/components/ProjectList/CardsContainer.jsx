import React from 'react';
import Select from 'react-select';
import Card from './ProjectsCards';
import projectList from './listOfProjects';
import './CardsContainer.css';
import 'react-select/dist/react-select.css';

export default class CardsContainer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: [],
      filterList: projectList
    }
    this.setTags = new Set();
    this.filterOptions = [];
    for (let i = 0; i < projectList.length; i++) {
      if (projectList[i].tags) {
        projectList[i].tags.forEach(tag => {
          projectList[i].tags.sort()
          this.setTags.add(tag.toLowerCase())
        })
      }
    }
    this.setTags.forEach(v => this.filterOptions.push({ value: v, label: v }));
    this.handleSelectChange = this.handleSelectChange.bind(this);
  }
  handleSelectChange(value) {
    this.setState({ value });
    this.handleFilterListUpdate(value);
  }
  handleFilterListUpdate(value) {
    if (value.length === 0) {
      return this.setState({ filterList: projectList });
    }
    let valueList = [];
    let updatedList = [];

    value.map(v => { 
      return valueList.push(v.value) 
    });
    projectList.map(project => {
      if (!project.tags) return;
      let lowerCaseTags = project.tags.map(v => v.toLowerCase())
      if (valueList.every(v => lowerCaseTags.includes(v))) {
        updatedList.push(project);
      }
    })
    this.setState({ filterList: updatedList});
  }
  render() {
    return (
      <div>
        <Select
          name="tag-selector"
          value={this.state.value}
          onChange={this.handleSelectChange}
          options={this.filterOptions}
          multi={true}
        />
        <section id='project-list' className='Container-layout'>
          { this.state.filterList.map((item, key) => {
            return (  
              <Card
                key={key}
                name={item.name}
                logoLink={item.imageSrc}
                githubLink={item.githubLink}
                description={item.description}
                tags={item.tags}
              />
            );
          })}
        </section>
      </div>
    );
  }
}
