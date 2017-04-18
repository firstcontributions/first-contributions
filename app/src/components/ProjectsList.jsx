import React from 'react';
import Card from './Card';
import ListOfProjects from './ListOfPorjects';
import SearchInput from './SearchInput';

class ProjectsList extends Component {
    constructor(props){
        super(props);

        this.state = {
            projects: ListOfProjects,
            searchValue: ""
        };

        this.displayFiltered = this.displayFiltered.bind(this);
        this.getSearchValue = this.getSearchValue.bind(this);
    }
    
    getSearchValue(newValue){
        this.setState({searchValue: newValue});
    }

    displayFiltered(){
        return(
            
        );
    }

    render() {
        return (
            <div>
                <SearchInput passValueUp={this.getSearchValue}/>
                {displayFiltered()}
            </div>
        );
    }
}

export default ProjectsList;