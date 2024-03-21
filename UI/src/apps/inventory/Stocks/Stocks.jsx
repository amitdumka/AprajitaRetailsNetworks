import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './Stocks.styles';

class Stocks extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('Stocks will mount');
  }

  componentDidMount = () => {
    console.log('Stocks mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('Stocks will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('Stocks will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('Stocks did update');
  }

  componentWillUnmount = () => {
    console.log('Stocks will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="StocksWrapper">
        Test content
      </div>
    );
  }
}

Stocks.propTypes = {
  // bla: PropTypes.string,
};

Stocks.defaultProps = {
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
)(Stocks);
