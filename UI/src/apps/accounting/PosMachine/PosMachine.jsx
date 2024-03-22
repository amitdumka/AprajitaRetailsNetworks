import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './PosMachine.styles';

class PosMachine extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('PosMachine will mount');
  }

  componentDidMount = () => {
    console.log('PosMachine mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('PosMachine will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('PosMachine will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('PosMachine did update');
  }

  componentWillUnmount = () => {
    console.log('PosMachine will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="PosMachineWrapper">
        Test content
      </div>
    );
  }
}

PosMachine.propTypes = {
  // bla: PropTypes.string,
};

PosMachine.defaultProps = {
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
)(PosMachine);
