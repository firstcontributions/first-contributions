import React, { Component } from 'react';

class SearchInput extends Component {
    constructor(props){
        super(props);

        this.state = {
            value: ""
        }

        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event){
        this.setState({value: event.target.value})
        this.props.passValueUp(this.state.value);
    }

    render() {
        return (
            <div className="">
                <h3 className="">Search: </h3>
                <input className=""type="text" value={this.state.value} onChange={this.handleChange}/>
            </div>
        );
    }
}

export default SearchInput;

