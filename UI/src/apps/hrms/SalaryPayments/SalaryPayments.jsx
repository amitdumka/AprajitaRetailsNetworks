import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './SalaryPayments.styles';

class SalaryPayments extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('SalaryPayments will mount');
  }

  componentDidMount = () => {
    console.log('SalaryPayments mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('SalaryPayments will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('SalaryPayments will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('SalaryPayments did update');
  }

  componentWillUnmount = () => {
    console.log('SalaryPayments will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="SalaryPaymentsWrapper">
        Test content
      </div>
    );
  }
}

SalaryPayments.propTypes = {
  // bla: PropTypes.string,
};

SalaryPayments.defaultProps = {
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
)(SalaryPayments);
