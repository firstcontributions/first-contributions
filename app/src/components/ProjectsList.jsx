import React, { Component } from 'react';
import Card from './Card';
import ListOfProjects from './ListOfProjects';
import SearchInput from './SearchInput';
import "./ProjectsList.css";

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