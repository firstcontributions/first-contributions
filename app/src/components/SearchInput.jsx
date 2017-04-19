import React, { Component } from 'react';

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

