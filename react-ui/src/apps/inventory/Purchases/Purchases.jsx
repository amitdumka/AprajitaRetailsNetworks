import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './Purchases.styles';

class Purchases extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('Purchases will mount');
  }

  componentDidMount = () => {
    console.log('Purchases mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('Purchases will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('Purchases will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('Purchases did update');
  }

  componentWillUnmount = () => {
    console.log('Purchases will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="PurchasesWrapper">
        Test content
      </div>
    );
  }
}

Purchases.propTypes = {
  // bla: PropTypes.string,
};

Purchases.defaultProps = {
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
)(Purchases);
