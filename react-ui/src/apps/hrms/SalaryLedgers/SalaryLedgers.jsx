import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './SalaryLedgers.styles';

class SalaryLedgers extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('SalaryLedgers will mount');
  }

  componentDidMount = () => {
    console.log('SalaryLedgers mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('SalaryLedgers will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('SalaryLedgers will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('SalaryLedgers did update');
  }

  componentWillUnmount = () => {
    console.log('SalaryLedgers will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="SalaryLedgersWrapper">
        Test content
      </div>
    );
  }
}

SalaryLedgers.propTypes = {
  // bla: PropTypes.string,
};

SalaryLedgers.defaultProps = {
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
)(SalaryLedgers);
