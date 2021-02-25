import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getCases, deleteCase } from "../../actions/cases";

export class Cases extends Component {
  static propTypes = {
    cases: PropTypes.array.isRequired,
    getCases: PropTypes.func.isRequired,
    deleteCase: PropTypes.func.isRequired,
  };

  componentDidMount() {
    this.props.getCases();
  }

  render() {
    return (
      <Fragment>
        <h2>Cases</h2>
        <div className="table-responsive">
          <table className="table table-striped">
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Message</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              {this.props.cases.map((cases) => (
                <tr key={cases.id}>
                  <td>{cases.id}</td>
                  <td>{cases.name}</td>
                  <td>{cases.email}</td>
                  <td>{cases.message}</td>
                  <td>
                    <button
                      onClick={this.props.deleteCase.bind(this, cases.id)}
                      className="btn btn-danger btn-sm"
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Fragment>
    );
  }
}

const mapStateToProps = (state) => ({
  cases: state.cases.cases,
});

export default connect(mapStateToProps, { getCases, deleteCase })(Cases);
