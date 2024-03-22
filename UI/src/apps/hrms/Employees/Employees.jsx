import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './Employees.styles';

class Employees extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('Employees will mount');
  }

  componentDidMount = () => {
    console.log('Employees mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('Employees will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('Employees will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('Employees did update');
  }

  componentWillUnmount = () => {
    console.log('Employees will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="EmployeesWrapper">
        Test content
      </div>
    );
  }
}

Employees.propTypes = {
  // bla: PropTypes.string,
};

Employees.defaultProps = {
  // bla: 'test',
};

const mapStateToProps = state => ({
  // blabla: state.blabla,
});

const mapDispatchToProps = dispatch => ({
  // fnBlaBla: () => dispatch(action.name()),
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(Employees);
