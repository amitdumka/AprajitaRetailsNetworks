import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './SaleReturns.styles';

class SaleReturns extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('SaleReturns will mount');
  }

  componentDidMount = () => {
    console.log('SaleReturns mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('SaleReturns will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('SaleReturns will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('SaleReturns did update');
  }

  componentWillUnmount = () => {
    console.log('SaleReturns will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="SaleReturnsWrapper">
        Test content
      </div>
    );
  }
}

SaleReturns.propTypes = {
  // bla: PropTypes.string,
};

SaleReturns.defaultProps = {
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
)(SaleReturns);
