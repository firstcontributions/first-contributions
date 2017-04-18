import React, { Component } from 'react';
import Card from './Card';
import ListOfProjects from './ListOfProjects';
import SearchInput from './SearchInput';

class ProjectsList extends Component {
    constructor(props){
        super(props);

        this.state = {
            projects: ListOfProjects,
            searchValue: ""
        };

        this.renderCard = this.renderCard.bind(this);
        this.displayFiltered = this.displayFiltered.bind(this);
        this.getSearchValue = this.getSearchValue.bind(this);
    }
    
    getSearchValue(newValue){
        this.setState({searchValue: newValue});
    }

    renderCard(dataObj){
        return(<Card Info={dataObj}/>);
    }

    displayFiltered(){
        return(
            <div>
                {this.state.projects.map((comp, index) => (
                    this.renderCard(comp)
                ))}
            </div>
        );
    }

    render() {
        return (
            <div>
                <SearchInput passValueUp={this.getSearchValue}/>
                {this.displayFiltered()}
            </div>
        );
    }
}

export default ProjectsList;