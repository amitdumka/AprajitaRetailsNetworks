import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './Sales.styles';

class Sales extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('Sales will mount');
  }

  componentDidMount = () => {
    console.log('Sales mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('Sales will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('Sales will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('Sales did update');
  }

  componentWillUnmount = () => {
    console.log('Sales will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="SalesWrapper">
        Test content
      </div>
    );
  }
}

Sales.propTypes = {
  // bla: PropTypes.string,
};

Sales.defaultProps = {
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
)(Sales);
