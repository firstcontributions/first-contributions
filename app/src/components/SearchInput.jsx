import React, { Component } from 'react';

/**
 * This is a component with state. It is used in the ProjectsList Class to allow the user to 
 * enter information. A function is passed down from the ProjectsList class, which allows the
 * value of the input to be passed up.
 */
class SearchInput extends Component {
    constructor(props){
        super(props);

        this.state = {
            value: ""
        }

        this.handleChange = this.handleChange.bind(this);
        this.submit = this.submit.bind(this);
    }

    handleChange(event){
        this.setState({value: event.target.value})
    }

    /**
     * Runs the passed down function when called.
     */
    submit(){
        this.props.passValueUp(this.state.value);
    }

    render() {
        return (
            <div className="RowContainer">
                <input className="" type="text" value={this.state.value} onChange={this.handleChange}/>
                <button onClick={this.submit}>Filter</button>
            </div>
        );
    }
}

export default SearchInput;

