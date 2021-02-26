import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addCase } from "../../actions/cases";

export class Form extends Component {
  state = {
    name: "",
    embg: "",
    message: "",
  };

  static propTypes = {
    addCase: PropTypes.func.isRequired,
  };

  onChange = (e) => this.setState({ [e.target.name]: e.target.value });
  onSubmit = (e) => {
    e.preventDefault();
    const { name, embg, message } = this.state;
    const cases = { name, embg, message };
    this.props.addCase(cases);
    this.setState({
      name: "",
      embg: "",
      message: "",
    });
  };

  render() {
    const { name, embg, message } = this.state;
    return (
      <div className="container">
        <div className="card card-body card-transparent mt-4 mb-4 mx-auto w-75">
          <h2 className="text-center">Add Case</h2>
          <form onSubmit={this.onSubmit}>
            <div className="form-group">
              <label>Name</label>
              <input
                className="form-control"
                type="text"
                name="name"
                onChange={this.onChange}
                value={name}
              />
            </div>
            <div className="form-group">
              <label>EMBG</label>
              <input
                className="form-control"
                type="text"
                name="embg"
                onChange={this.onChange}
                value={embg}
              />
            </div>
            <div className="form-group">
              <label>Message</label>
              <input
                className="form-control"
                type="text"
                name="message"
                onChange={this.onChange}
                value={message}
              />
            </div>
            <div className="form-group">
              <button type="submit" className="btn background-dark-purple">
                Submit
              </button>
            </div>
          </form>
        </div>
      </div>
    );
  }
}

export default connect(null, { addCase })(Form);
