import React, { Component } from 'react';
import Card from './Card';
import ListOfProjects from './ListOfProjects';
import SearchInput from './SearchInput';
import "./ProjectsList.css";

/**
 * This is the component which will hold many cards (project info card). A array
 * of projects is passed in from ListOfProjects. The state holds the full list of projects
 * and then there is a tempList key which holds the value of the current list based on the 
 * search ( this is initialized to all the projects )
 */
class ProjectsList extends Component {
    constructor(props){
        super(props);

        this.state = {
            projects: ListOfProjects,
            tempList: ListOfProjects,
            searchValue: ""
        };

        this.getSearchValue = this.getSearchValue.bind(this);
    }
    
    /**
     * Function that is passed down to the search component which allows the search
     * component to pass in a value that was searched for and this is then passed into
     * the state here.
     * @param {*} newValue 
     */
    getSearchValue(newValue){
        this.setState({searchValue: newValue});
        let arr = [];
        for(let i = 0; i < this.state.projects.length; i++){
            if(this.state.projects[i].keywords.indexOf(this.state.searchValue) != -1){
                arr.push(this.state.projects[i]);
            }
        }
        this.setState({tempList: arr});
    }

    // The tempList found in state is mapped into the div, with for each object in the array
    // creating a Card component from it.
    render() {
        return (
            <div className="ColumnContainer">
                <SearchInput passValueUp={this.getSearchValue}/>
                <div className="RowContainer">
                    {this.state.tempList.map((item, index)=>(
                        <Card Info={item} />
                    ))}
                </div>
            </div>
        );
    }
}

export default ProjectsList;